#========================================
#    author: hanjuntai
#      mail: hanjuntai@yeah.net
#      time: 13/05/2020
#========================================
from System import *
from Deadline.Events import *
from Deadline.Scripting import *
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def GetDeadlineEventListener():
    return OverrideJobPriorityListener()


def CleanupDeadlineEventListener(eventListener):
    return eventListener.Cleanup()


class OverrideJobPriorityListener(DeadlineEventListener):
    '''
    '''

    def __init__(self):
        '''
        '''
        self.OnJobSubmittedCallback += self.OnJobSubmitted



    def Cleanup(self):
        '''
        '''
        del self.OnJobSubmittedCallback


    def OnJobSubmitted(self, job):
        '''
        '''
        job.Priority = min(50, job.Priority)
        RepositoryUtils.SaveJob(job)
