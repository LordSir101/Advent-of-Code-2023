#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include<vector>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;

int main () {
  string line;
  ifstream myfile ("input.txt");
  if (myfile.is_open())
  {

    string times;
    string records;
    int line_num = 1;
    while(getline(myfile, line)) {
      std::string token = line.substr(line.find(":") + 1, line.size());
      std::string::iterator end_pos = std::remove(token.begin(), token.end(), ' ');
      token.erase(end_pos, token.end());
      int number;
      if(line_num == 1){
        times = token;
      }
      else{
        records = token;
      }
        
        line_num++;
    }
    
    int a = -1;
    long b = stol(times);
    long c = (stol(records)+1) * -1;
    
    double dis = sqrt(pow(b,2) - (4*a*c));
    
    double r1 = (-1*b+ dis) / 2*a;
    double r2 = (-1*b - dis) / 2*a;
    
    long lowest = ceil(min(r1,r2));
    long highest = floor(max(r1,r2));
    
    long total = highest - lowest + 1;
    
    cout << total << endl;
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
    