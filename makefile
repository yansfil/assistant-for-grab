app/client/.install.stamp: app/client/package.json app/client/pnpm-lock.yaml
	@echo "Installing client dependencies..."
	cd app/client && pnpm install --no-frozen-lockfile
	touch .client_deps.stamp

app/server/.install.stamp: app/server/pyproject.toml app/server/poetry.lock
	@echo "Installing server dependencies..."
	cd app/server && poetry install
	touch .server_deps.stamp


.PHONY: install-deps 
install-deps: app/client/.install.stamp app/server/.install.stamp

.PHONY: watch-dev
watch-dev: install-deps
	@echo "Starting client and server with PM2..."
	pm2 cleardump
	pm2 flush
	bash -c "trap 'make stop-watch-dev' EXIT; \
	         pm2 logs & \
	         pm2 start; \
	         wait"

.PHONY: stop-watch-dev
stop-watch-dev:
	@echo "Stopping all PM2 processes..."
	pm2 stop all || :
	pm2 kill
