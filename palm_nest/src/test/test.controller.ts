import { Controller, Post, Get, Body, Query, Res } from '@nestjs/common';
import { TestService } from './test.service';
import { Student } from './student.entity';
import { Response } from 'express';

@Controller('api/test')
export class TestController {
  constructor(private readonly testService: TestService) {}

  @Post('test_post')
  async createStudent(
    @Body() student: Partial<Student>,
    @Res() res: Response,
  ): Promise<void> {
    try {
      const createdStudent = await this.testService.createStudent(student);
      res.status(201).json({
        status: 'success',
        data: {
          name: createdStudent.name,
          age: createdStudent.age,
          grade: createdStudent.grade,
        },
      });
    } catch (error) {
      res.status(500).json({
        status: 'error',
        message: 'Internal server error',
      });
    }
  }

  @Get('test_get')
  async findStudentByName(
    @Query('name') name: string,
    @Res() res: Response,
  ): Promise<void> {
    try {
      const students = await this.testService.findStudentByName(name);
      if (students.length > 0) {
        const studentData = students[0]; // 假设查询结果只返回一个学生
        res.status(200).json({
          status: 'success',
          data: {
            name: studentData.name,
            age: studentData.age,
            grade: studentData.grade,
          },
        });
      } else {
        res.status(404).json({
          status: 'error',
          message: 'Student not found',
        });
      }
    } catch (error) {
      res.status(500).json({
        status: 'error',
        message: 'Internal server error',
      });
    }
  }
}
