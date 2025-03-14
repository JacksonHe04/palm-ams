// src/management/controllers/apply.controller.ts
import { Controller, Get } from '@nestjs/common';
import { ApplyService } from './admin.service';
import { Apply } from './entities/students.entity';

@Controller('api/students')
export class ApplyController {
  constructor(private readonly applyService: ApplyService) {}

  @Get()
  async getStudents(): Promise<Apply[]> {
    return this.applyService.findAll();
  }
}
