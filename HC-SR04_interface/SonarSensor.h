#pragma once
#include<wiringPi.h>
#include<sys/time.h>

class SonarSensor{
	public:
	SonarSensor(int Trig, int Echo);
	int Trig ,Echo;
	int GetReadings();
	volatile long startTimeUsec, endTimeUsec;
	long now, timeout = 38000.0, distance, duration;
	
};
