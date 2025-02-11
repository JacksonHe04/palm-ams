// src/admin/admin.module.ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ApplyController } from './admin.controller';
import { ApplyService } from './admin.service';
import { Apply } from './entities/students.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Apply])],
  controllers: [ApplyController],
  providers: [ApplyService],
})
export class AdminModule {}
