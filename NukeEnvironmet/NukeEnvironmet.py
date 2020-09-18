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
    eventListener.Cleanup()


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
        if job.JobPlugin == 'Nuke':
            job.SetJobEnvironmentKeyValue('foundry_LICENSE',  '5053@lic.ds.com')
            job.SetJobEnvironmentKeyValue('NUKE_PATH',  '//oct.ds.com/TD/Tools/NUKEScripts/Nuke_plugins_Oct')
            RepositoryUtils.SaveJob(job)
