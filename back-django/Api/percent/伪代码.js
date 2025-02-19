import Apply from Api.apply.models
import Major from Api.setting.models
import Award from Api.setting.models
import Year from Api.setting.models
import Percent from Api.percent.models

let result = [];
const currYear = Year.year;
从Percent里面拿percentOfA

const filterTalent = function(student) {
  if(student.paper1_isFirst) {
    if(student.paper1_ccfLevel == "A" || student.paper1_ccfLevel == "B") {
      student.isPaperCondition = true;
    }
  } else if (student.paper2_isFirst) {
    if(student.paper2_ccfLevel == "A" || student.paper2_ccfLevel == "B") {
      student.isPaperCondition = true;
    }
  } else if (student.paper3_isFirst) {
    if(student.paper3_ccfLevel == "A" || student.paper3_ccfLevel == "B") {
      student.isPaperCondition = true;
    }
  } else student.isPaperCondition = false;

  const awards = [[award1_isLeader, award1_name, award1_awardRanking], [award2_isLeader, award2_name, award2_awardRanking], [award3_isLeader, award3_name, award3_awardRanking]]
  let student.isAwardCondition = false;
  for(对于awards里的award) {
    if(award[0] == true) {
      if(去Award里去找有没有Award的name是award[1]且该Award.category == "限制奖项"且award[2] == "特等奖"或"金奖"){
        student.isAwardCondition = true;
      }
    }
  }

  if(isPaperCondition || isAwardCondition) {
    return true;
  } else return false;
}

const filterMajor(student) {
  if(去Major里去找有没有 Major的 name是student.major 且该Major.category == "限制专业") {
    return true;
  } else if(去Major里去找有没有 Major的 name是student.masterMajor 且该Major.category == "限制专业") {
    return true;
  } else {
    return false;
  }
}
  
const filterEachStudent = function(student) {
  if(student.year = currYear) {
    const p = student.pencentage.(去掉"%"并转为数字类型);
    
    if(student.universityLevel == "A" || student.masterLevel == "A") {
      if(p <= pOfA) {
        student.isFilterCondition = true;
        return student;
      }
      if(student.isTopClass && p <= pOfATop) {
        student.isFilterCondition = true;
        return student;
      }
      if(filterTalent(student) && p <= pOfATalent) {
        student.isFilterCondition = true;
        return student;
      }
    }

    if(student.universityLevel == "B" || student.masterLevel == "B") {
      if(p <= pOfB && filterMajor(student)) {
        student.isFilterCondition = true;
        return student;
      }
      if(student.isTopClass && p <= pOfBTop) {
        student.isFilterCondition = true;
        return student;
      }
      if(filterTalent(student) && p <= pOfBTalent) {
        student.isFilterCondition = true;
        return student;
      }
    }

    if(student.universityLevel == "C" || student.masterLevel == "C") {
      if(p <= pOfC && filterMajor(student)) {
        student.isFilterCondition = true;
        return student;
      }
      if(student.isTopClass && p <= pOfCTop) {
        student.isFilterCondition = true;
        return student;
      }
      if(filterTalent(student) && p <= pOfCTalent) {
        student.isFilterCondition = true;
        return student;
      }
    } 
  }  
}
  
for (let student in Apply Apply模型里的所有学生) {
  result.push(filterEachStudent(student));
}
