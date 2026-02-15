import { logger } from './logger';
import { config } from './config';
import { App } from './app';

async function main() {
  try {
    const app = new App(config);
    await app.init();
    app.start();
  } catch (error: any) {
    logger.error('Error starting application', error);
    process.exit(1);
  }
}

process.on('SIGTERM', () => {
  logger.info('Received SIGTERM, exiting...');
  process.exit(0);
});

process.on('uncaughtException', (error: any) => {
  logger.error('Uncaught exception', error);
  process.exit(1);
});

main();
