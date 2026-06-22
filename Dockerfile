# ── Stage 1: Build dependencies ───────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

# Install system deps for Playwright browser download and extraction
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download chromium browser and its system dependencies cleanly
RUN playwright install --with-deps chromium

# ── Stage 2: Production image ─────────────────────────────────────
FROM python:3.12-slim

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser -s /sbin/nologin appuser

# Set environment variable for Playwright browser path
ENV PLAYWRIGHT_BROWSERS_PATH=/home/appuser/.cache/ms-playwright

# Copy installed packages and Playwright browsers from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /root/.cache/ms-playwright /home/appuser/.cache/ms-playwright

# Install Playwright system deps and curl/ca-certificates in production image
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libxss1 \
    libxtst6 \
    libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

# Copy source code
COPY . .

# Fix ownership for non-root user
RUN chown -R appuser:appuser /app /home/appuser

# Switch to non-root user
USER appuser

# Expose port (can be overridden by PORT env var)
EXPOSE 8000

# Use PORT env var if set (for cloud platforms), fallback to 8000
ENV PORT=8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

# Run server
CMD uvicorn server.app:app --host 0.0.0.0 --port $PORT
