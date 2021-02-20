#include "SonarSensor.h"

SonarSensor::SonarSensor(int Trig, int Echo){
	wiringPiSetup();
	pinMode(Trig, OUTPUT);
	pinMode(Echo, INPUT);
	this->Trig = Trig;
	this->Echo = Echo;
}

int SonarSensor::GetReadings(){
	digitalWrite(Trig, 0);
	digitalWrite(Echo, 0);
	delayMicroseconds(2);
	digitalWrite(Trig, 1);
	delayMicroseconds(10);
	now = micros();
	
		while(digitalRead(Echo) == 0 && micros()-now<timeout);
		
		startTimeUsec = micros();
        while ( digitalRead(Echo) == HIGH );
        endTimeUsec = micros();
        
	duration = endTimeUsec - startTimeUsec;
	distance = 100*((duration/1000000.0)*340.29)/2;
	distance =(duration*0.034/2);
	delay(500);
	return distance;
}
