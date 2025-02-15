// src/management/services/apply.service.ts
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Apply } from './entities/students.entity';

@Injectable()
export class ApplyService {
  constructor(
    @InjectRepository(Apply)
    private readonly applyRepository: Repository<Apply>,
  ) {}

  async findAll(): Promise<Apply[]> {
    const applies = await this.applyRepository.find();

    return applies.map((apply) => ({
      ...apply,
      papers: [
        {
          publicationTime: apply.paper1_publicationTime || null,
          journalConference: apply.paper1_journalConference || null,
          paperName: apply.paper1_paperName || null,
          ccfLevel: apply.paper1_ccfLevel || null,
        },
        {
          publicationTime: apply.paper2_publicationTime || null,
          journalConference: apply.paper2_journalConference || null,
          paperName: apply.paper2_paperName || null,
          ccfLevel: apply.paper2_ccfLevel || null,
        },
        {
          publicationTime: apply.paper3_publicationTime || null,
          journalConference: apply.paper3_journalConference || null,
          paperName: apply.paper3_paperName || null,
          ccfLevel: apply.paper3_ccfLevel || null,
        },
      ],
      awards: [
        {
          isLeader:
            apply.award1_isLeader !== undefined ? apply.award1_isLeader : null,
          awardTime: apply.award1_awardTime || null,
          awardName: apply.award1_awardName || null,
          levelRanking: apply.award1_levelRanking || null,
          awardRanking: apply.award1_awardRanking || null,
        },
        {
          isLeader:
            apply.award2_isLeader !== undefined ? apply.award2_isLeader : null,
          awardTime: apply.award2_awardTime || null,
          awardName: apply.award2_awardName || null,
          levelRanking: apply.award2_levelRanking || null,
          awardRanking: apply.award2_awardRanking || null,
        },
        {
          isLeader:
            apply.award3_isLeader !== undefined ? apply.award3_isLeader : null,
          awardTime: apply.award3_awardTime || null,
          awardName: apply.award3_awardName || null,
          levelRanking: apply.award3_levelRanking || null,
          awardRanking: apply.award3_awardRanking || null,
        },
      ],
      universityLevel: apply.universityLevel || null,
      masterUniversityLevel: apply.masterUniversityLevel || null,
    }));
  }
}
