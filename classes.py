class OneExit:
    def __init__(self):
        self.begin_score = 0
        self.user_id = 0
        self.username =0
        self.chat_id = 0
        self.datetime = 0
        self.zone = 0
        self.end_score = 0
        self.level = 0
        self.emotion = ''
        self.helper = ''
        self.location = ''
        self.resource = ''
        self.wish = ''
        self.error = ''
        self.change_plus = ''
        self.change_minus = ''

    def print_session(self):
        print('begin_score', self.begin_score)
        print('user_id', self.user_id)
        print('username', self.username)
        print('chat_id', self.chat_id)
        print(self.datetime)
        print(self.zone)
        print('end_score', self.end_score)
        print('level', self.level)
        print('emotion', self.emotion)
        print('helper', self.helper)
        print('location', self.location)
        print('resource', self.resource)
        print('wish', self.wish)
        print('error', self.error)
        print('plus', self.change_plus)
        print('minus', self.change_minus)
    def to_json(self):
        dict = {}
        dict['begin_score'] = self.begin_score
        dict['user_id'] = self.user_id
        dict['username'] = self.username
        dict['chat_id'] = self.chat_id
        dict['datetime'] = self.datetime
        dict['zone'] = self.zone
        dict['end_score'] = self.end_score
        dict['level'] = self.level
        dict['emotion'] = self.emotion
        dict['helper'] = self.helper
        dict['location'] = self.location
        dict['resource'] = self.resource
        dict['wish'] = self.wish
        dict['error'] = self.error
        dict['change_plus'] = self.change_plus
        dict['change_minus'] = self.change_minus
        return dict

class Answers:
    def __init__(self):
        self.level1_angry = ['все они плохие, только ты хороший',
                    'да как они могли так поступить!',
                    'наверное, они не смогли тебя понять',
                    'какие же бывают плохие люди вокруг',
                    'они неправы, они просто тебя не поняли',
                    'сложно жить, когда тебя не ценят по достоинству'
                    ]