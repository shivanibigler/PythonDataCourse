import datajoint as dj

schema = dj.schema('dummyhomework')


@schema
class MouseSubject(dj.Manual):
    definition = """
    # some mouse table
    subject_id : int  # id for mouse subject
    ---
    age : float # age of mouse in weeks
    sex = 'U': enum('F', 'M', 'U')  # sex of mouse
    comments = null : varchar(4000)
    """
    
    
@schema
class OdorStimulus(dj.Manual):
    definition = """
    # stimulus table
    stimulus_name : varchar(31) # short name for stimulus
    ---
    stimulus_type : enum('social', 'nonsocial')
    duration : float # in seconds
    """
    
    
@schema
class TestingSession(dj.Manual):
    definition = """
    # record them sessions
    -> MouseSubject
    recording_id : int 
    ---
    -> OdorStimulus
    experimenter : varchar(127)
    improvement : enum('learned', 'stagnant', 'dumb')
    comments = null : varchar(4000)
    """