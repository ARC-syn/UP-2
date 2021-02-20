#include "SonarSensor.h"
#include <iostream>
using namespace std;

int main(){
	int result;
	SonarSensor MainSensor(28, 29);
	result = MainSensor.GetReadings();
	std::cout << result;
	return 0;
}
