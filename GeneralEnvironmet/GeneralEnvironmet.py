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
    return MayaEnvListener()


def CleanupDeadlineEventListener(eventListener):
    return eventListener.Cleanup()


class MayaEnvListener(DeadlineEventListener):
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
        job.SetJobEnvironmentKeyValue('REZ_CONFIG_FILE',    '//192.168.15.15/pipeline/config/rezconfig.py')
        RepositoryUtils.SaveJob(job)
