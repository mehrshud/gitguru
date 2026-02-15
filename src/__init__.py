import { createLogger, format, transports } from 'winston';
import { GraphQLServer } from 'graphql-yoga';
import { Config } from './config';
import { schema } from './schema';

const logger = createLogger({
  level: Config.logLevel,
  format: format.json(),
  transports: [new transports.Console()],
});

async function main() {
  try {
    const server = new GraphQLServer({ schema });
    await server.start();
    logger.info(`Server started on port ${Config.port}`);
  } catch (error) {
    logger.error('Failed to start server', error);
    process.exit(1);
  }
}

main();
