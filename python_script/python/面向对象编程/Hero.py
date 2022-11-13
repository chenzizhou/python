class Hero:
    def __init__(self,name,*argu,words):
        if len(argu)==1:
            self.skill1=argu
        elif len(argu)==2:
            self.skill1,self.skill2=argu
        elif len(argu)==3:
            self.skill1,self.skill2,self.skill3=argu
        else:   
            self.skill1,self.skill2,self.skill3,self.skill4=argu
        self.name=name
        self.words=words
zgl=Hero('zgl','一技能','二技能',words='人生如棋，一步三算')
print(zgl.skill1,zgl.skill2,zgl.words)