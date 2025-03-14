// src/app/app.module.ts
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { HomeModule } from '../home/home.module';
import { AuthModule } from '../auth/auth.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { TestModule } from '../test/test.module';
import { AdminModule } from '../admin/admin.module';
import { ApplyModule } from '../apply/apply.module';

@Module({
  imports: [HomeModule, AuthModule, TestModule, AdminModule, ApplyModule,
  TypeOrmModule.forRoot({
    type: 'mysql',
    host: 'localhost',
    port: 3306,
    username: 'root',
    password: '123456',
    database: 'palm_apply',
    entities: ['dist/**/*.entity{.ts,.js}'],
    synchronize: true,
    logging: true,
  })],
  controllers: [AppController],
})
export class AppModule {}
