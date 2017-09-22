#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Point {
 public:
    Point(int x_, int y_)
        : start(x_), end(y_)
    {}

    int start;
    int end;
};

int intersect_val(std::vector<Point> v) {
    Point cIn = v[0];
    for (size_t i = 1; i < v.size(); i++) {
        if (cIn.end < v[i].start || cIn.start > v[i].end) {
            return 0;
        }
        cIn = Point(max(cIn.start,v[i].start), min(cIn.end, v[i].end));
    }
    return abs(cIn.end - cIn.start);
}

int main() {

    int tc = scanf("%d", &tc);
    while(tc != 0) {
        vector<Point> x;
        vector<Point> y;
        vector<Point> z;
        for (size_t i = 0; i < tc; i++) {
            int tempx=0, tempy=0, tempz=0, templ=0;
            cin >> tempx >> tempy >> tempz >> templ;
            x.push_back(Point(tempx, tempx + templ));
            y.push_back(Point(tempy, tempy + templ));
            z.push_back(Point(tempz, tempz + templ));
            printf("%d %d %d",tempx, tempy, tempz);
        }

        // printf("%d\n", (intersect_val(x)*intersect_val(y)*intersect_val(z)));


        tc = scanf("%d", &tc);
    }

    // printf("%s %d\n", "this number was in the input file:", d);
    return 0;
}
