class Activity:
  def __init__(self, name,date,duration,action,channel_id,channel_name, result, mood):
        self.name = name
        self.date = date
        self.duration = duration
        self.action = action
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.result = result
        self.mood = mood
  def to_dict(self):
    return {
            'name': self.name,
            'date': self.date,
            'duration': self.duration,
            'action': self.action,
            'channel_id': self.channel_id,
            'channel_name': self.channel_name,
            'result': self.result,
            'mood': self.mood
        }
  @staticmethod
  def from_dict(data):
    return Activity(
            name=data['name'],
            date=data['date'],
            duration=data['duration'],
            action=data['action'],
            channel_id=data['channel_id'],
            channel_name=data['channel_name'],
            result=data['result'],
            mood=data['mood']
        )
  
     
       


def get_activities():
  activities = [
    { "channelId": '1106018346140454925', "name": '小熊spa店💆' },
    { "channelId": '1106025814107103262', "name": '小熊网吧🖥' },
    { "channelId": '1105770785261506661', "name": '反省室' },
    { "channelId": '1109558764387979294', "name": '小熊艺术中心' },
    { "channelId": '1105757762526400512', "name": '小狗房🐕' },
    { "channelId": '1105759395159228468', "name": '小熊淋浴间2号' },
    { "channelId": '1109554624823824535', "name": '小熊图书馆' },
    { "channelId": '1106238225309253723', "name": '小熊的花园' },
    { "channelId": '1091581674011238430', "name": '小熊淋浴间1号' },
    { "channelId": '1109558927265366107', "name": '小熊科学实验室' },
    { "channelId": '1106397292484894751', "name": '烘焙店🎂' },
    { "channelId": '1109558798324092948', "name": '小熊音乐房' },
    { "channelId": '1109558723942301717', "name": '小熊烹饪教室' },
    { "channelId": '1105760698807623680', "name": '🎡小熊游乐场🎇' },
    { "channelId": '1106641645253971988', "name": '小熊学校' },
    { "channelId": '1106237172366979152', "name": '保安室' },
    { "channelId": '1106642151489679501', "name": '小熊健身房' },
    { "channelId": '1105760499620122664', "name": '小熊电影院🎦' },
    { "channelId": '1105757733300490290', "name": '小猪房🐷' },
    { "channelId": '1109558686046748853', "name": '小熊工作室' },
    { "channelId": '1105760952433000458', "name": '小熊游泳池🏊' },
    { "channelId": '1106654870682996897', "name": '情趣套房' }
  ]
  activities_in_String = ""
  for activity in activities:
      activities_in_String += activity["name"] +  " channelId:"+ activity["channelId"] + "\n"
  return activities_in_String