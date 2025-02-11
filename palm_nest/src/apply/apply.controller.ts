// src/apply/apply.controller.ts
import { Controller, Post, Body } from '@nestjs/common';
import { ApplyService } from './apply.service';
import { Apply } from '../admin/entities/students.entity';

@Controller('api')
export class ApplyController {
  constructor(private readonly applyService: ApplyService) {}

  @Post('apply')
  async createApply(@Body() applyData: Apply) {
    return this.applyService.createApply(applyData);
  }
}
