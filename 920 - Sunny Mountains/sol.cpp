#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Point {
 public:
    Point(int x_, int y_)
        : x(x_), y(y_)
    {}

    double distance( const Point &point ) {
        return sqrt((x-point.x)*(x-point.x)+(y-point.y)*(y-point.y));
    }

    bool operator< (const Point &other) const {
        return x < other.x;
    }

 // private:
    int x;
    int y;
};

float length_of_sunshine(Point startP, Point endP, int h) {
    float dx = abs(startP.x - endP.x);
    float dy = abs(startP.y - endP.y);
    return sqrt(dx*dx + dy*dy) * (float(endP.y-h)/dy);
}

int main() {
    int test_case;
    scanf("%d", &test_case);

    for (size_t i = 0; i < test_case; i++) {
        vector<Point> points;
        int n, x=0, y=0;
        scanf("%d", &n);
        for (size_t i = 0; i < n; i++) {
            cin >> x >> y;
            Point p(x,y);
            points.push_back(p);
        }
        sort(points.rbegin(), points.rend());

        float total_length = 0;
        int current_height = 0;
        float j;
        for (size_t i = 0; i < n/2; i++) {
            if (current_height < points[2*i+1].y){
                j = length_of_sunshine(points[2*i], points[2*i+1], current_height);
                total_length += j;
                current_height = points[2*i+1].y;
            }
        }
        printf("%.2f\n", total_length);
    }

    return 0;
}
