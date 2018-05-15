import os
from threading import Thread

class Th(Thread):
	def __init__ (self, core, videos):
		Thread.__init__(self)
		self.core = core
		self.videos = []
		for video in videos.split("*"):
			self.videos.append(video)

	def run(self):
		qps = ['22','27','32','37']
		fps = {'Tango':60, 'Drums':100, 'CampfireParty':30, 'ToddlerFountain':60, 'CatRobot':60, 'TrafficFlow':30, 'DaylightRoad':60, 'RollerCoaster':60, 'Traffic':30, 'PeopleOnStreet':30, 'NebutaFestival_10bit':60, 'SteamLocomotiveTrain_10bit':60, 'Kimono':24, 'ParkScene':24, 'Cactus':50, 'BQTerrace':60, 'BasketballDrive':50}
		#fps = {'RaceHorsesC':30,'BQMall':60,'PartyScene':50,'BasketballDrill':50,'RaceHorses':30,'BQSquare':60,'BlowingBubbles':50,'BasketballPass':50,'FourPeople':60,'Johnny':60,'KristenAndSara':60,'BasketballDrillText':50,'ChinaSpeed':30,'SlideEditing':30,'SlideShow':20}
		cfg = {'Tango':'main10', 'Drums':'main10', 'CampfireParty':'main10', 'ToddlerFountain':'main10', 'CatRobot':'main10', 'TrafficFlow':'main10', 'DaylightRoad':'main10', 'RollerCoaster':'main10', 'Traffic':'main', 'PeopleOnStreet':'main', 'NebutaFestival_10bit':'main10', 'SteamLocomotiveTrain_10bit':'main10', 'Kimono':'main', 'ParkScene':'main', 'Cactus':'main', 'BQTerrace':'main', 'BasketballDrive':'main'}
		intraPeriod = {20:16, 24:32, 30:32, 50:48, 60:64, 100:96, 120:128}
		testCond = "RA" #RA, AI, LB

		for video in self.videos:
			ip = str(intraPeriod[fps[video]])
			encoderCfgFile = 'encoder_randomaccess_' + cfg[video] + '.cfg'

			for qp in qps:
				outFile = "outputs/" + testCond + "/" + video + "_" + qp + ".txt"
				bsFile = "outputs/" + testCond + "/STRs/str_" + video + "_" + qp + ".bin"

				#cmd = "taskset -c " + task + " ./bin/TAppEncoderStatic -c cfg/" + encoderCfgFile + " -c " + video + ".cfg --QP=\"" + qp + "\" --IntraPeriod=\"" + ip + "\" --BitstreamFile=\"" + bsFile + "\"  --ReconFile=\"\" > " + outFile
				cmd = "taskset -c " + self.core + " ./bin/TAppEncoderStatic -c cfg/" + encoderCfgFile + " -c myCFGs/" + video + ".cfg --QP=\"" + qp + "\" --IntraPeriod=\"" + ip + "\" --BitstreamFile=\"" + bsFile + "\"  --ReconFile=\"\" > " + outFile
				print cmd
				os.system(cmd)
				

#videos = ['Tango', 'Drums', 'CampfireParty', 'ToddlerFountain', 'CatRobot', 'TrafficFlow', 'DaylightRoad', 'RollerCoaster']
videos = ['Traffic','PeopleOnStreet', 'NebutaFestival_10bit', 'SteamLocomotiveTrain_10bit', 'Kimono*ParkScene', 'Cactus', 'BasketballDrive', 'BQTerrace']
core = 0
for video in videos:
	thread = Th(str(core), video)
	thread.start()
	core += 1