module.exports = {
  apps: [
    {
      name: "client",
      script: "pnpm run dev --port $CLIENT_PORT | pino-pretty",
      cwd: "./app/client",
      env: {
        CLIENT_PORT: 3000
      }
    },
    {
      name: "server",
      script: "poetry run uvicorn main:app --reload --host 0.0.0.0 | pino-pretty",
      cwd: "./app/server",
      env: {
        SERVER_PORT: 8000
      }
    }
  ]
};