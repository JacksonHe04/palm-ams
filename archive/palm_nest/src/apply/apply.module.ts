// src/apply/apply.module.ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ApplyService } from './apply.service';
import { ApplyController } from './apply.controller';
import { Apply } from '../admin/entities/students.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Apply])],
  providers: [ApplyService],
  controllers: [ApplyController]
})
export class ApplyModule {}
