#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int maxW = 0; int maxH = 0;
    int temp = 0;
    int w = 0; int h = 0;
    for (auto size : sizes)
    {
        w = size[0];
        h = size[1];
        if (w < h) {
            temp = w;
            w = h;
            h = temp;
        }
        if (w > maxW) maxW = w;
        if (h > maxH) maxH = h;
    }
    
    return maxW * maxH;
}