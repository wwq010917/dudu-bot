class Bear:
    def __init__(self, name):
        self.name = name
        self.mood = "平静"
        self.happy = 10
        self.location = "无"
        self.activity_log = []
       
    def change_mood(self, mood,effect):
        self.mood = mood
        self.happy += effect
        if self.happy > 10:
            self.happy = 10
        elif self.happy < 0:
            self.happy = 0

    def move_to_location(self, location):
        self.location = location
        
    def add_activity(self, activity):
        self.activity_log.append(activity)
    def remove_activity(self):
        if len(self.activity_log) >= 10:
            del self.activity_log[0]
    def reset_activity(self):
        self.activity_log = []
    def get_current_state(self):
        return {
            "name": self.name,
            "mood": self.mood,
            "happy": self.happy,
            "location": self.location,
            "activity_log": self.activity_log,
        }
    
