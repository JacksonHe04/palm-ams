// src/main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app/app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // 启用 CORS
  app.enableCors({
    origin: 'http://localhost:5173', // 前端开发服务器地址
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true, // 如果需要发送 cookies 或者认证信息
  });

  await app.listen(3000);
}
bootstrap();
