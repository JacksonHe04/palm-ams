import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Apply } from '../admin/entities/students.entity';

@Injectable()
export class ApplyService {
  constructor(
    @InjectRepository(Apply)
    private readonly applyRepository: Repository<Apply>,
  ) {}

  async createApply(applyData: any): Promise<any> {
    // 处理 papers 数组
    if (applyData.papers && applyData.papers.length > 0) {
      applyData.papers.forEach((paper: any, index: number) => {
        if (index < 3) { // 假设最多支持3篇论文
          applyData[`paper${index + 1}_publicationTime`] = paper.publicationTime;
          applyData[`paper${index + 1}_journalConference`] = paper.journalConference;
          applyData[`paper${index + 1}_paperName`] = paper.paperName;
          applyData[`paper${index + 1}_ccfLevel`] = paper.ccfLevel;
          applyData[`paper${index + 1}_awardCategory`] = paper.awardCategory;
        }
      });
    }

    // 处理 awards 数组
    if (applyData.awards && applyData.awards.length > 0) {
      applyData.awards.forEach((award: any, index: number) => {
        if (index < 3) { // 假设最多支持3个奖项
          applyData[`award${index + 1}_isLeader`] = award.isLeader;
          applyData[`award${index + 1}_awardTime`] = award.awardTime;
          applyData[`award${index + 1}_awardName`] = award.awardName;
          applyData[`award${index + 1}_levelRanking`] = award.levelRanking;
        }
      });
    }

    // 删除原始的 papers 和 awards 数组，避免保存到数据库中
    delete applyData.papers;
    delete applyData.awards;

    const newApply = this.applyRepository.create(applyData);
    const savedApplyResult = await this.applyRepository.save(newApply);

    // 如果 save 返回的是数组，则取第一个元素
    let savedApply: Apply;
    if (Array.isArray(savedApplyResult)) {
      savedApply = savedApplyResult[0];
    } else {
      savedApply = savedApplyResult;
    }

    // 获取当前时间并格式化
    const currentTime = new Date().toISOString().replace('T', '-').replace(/\..+/, '');

    // 构造返回的 JSON 对象
    const response = {
      message: "申请表单提交成功",
      data: {
        id: savedApply.id, // 确保 savedApply 是单个 Apply 实例
        time: currentTime
      }
    };

    return response;
  }
}

