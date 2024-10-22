# 导入第三方库
from crewai.flow.flow import Flow, listen, start
from crews.marketAnalystCrew.marketAnalystCrew import marketAnalystCrew
from crews.contentCreatorCrew.contentCreatorCrew import contentCreatorCrew


class workFlow(Flow):

    # 构造初始化函数，接受job_id作为参数，用于标识作业
    def __init__(self, job_id, llm, inputData):
        super().__init__()
        self.job_id = job_id
        self.llm = llm
        self.inputData = inputData

    @start()
    def marketAnalystCrew(self):
        result = marketAnalystCrew(self.job_id, self.llm, self.inputData).kickoff()
        print("marketAnalystCrew result:", result)
        return result

    @listen(marketAnalystCrew)
    def contentCreatorCrew(self):
        result = contentCreatorCrew(self.job_id, self.llm, self.inputData).kickoff()
        print("contentCreatorCrew result:", result)
        return result

