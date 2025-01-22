import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Student } from './student.entity';

@Injectable()
export class TestService {
  constructor(
    @InjectRepository(Student)
    private studentsRepository: Repository<Student>,
  ) {}

  async createStudent(student: Partial<Student>): Promise<Student> {
    return this.studentsRepository.save(student);
  }

  async findStudentByName(name: string): Promise<Student[]> {
    return this.studentsRepository.find({ where: { name } });
  }
}
