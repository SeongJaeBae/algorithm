#include <iostream>
#include <limits>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <utility>
#include <string>
#include <bitset>
#include <functional>
#include <chrono>
#include <random>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
using namespace std;

using base = complex<double>;

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using pil = pair<int, ll>;
using pli = pair<ll, int>;
using pll = pair<ll, ll>;

using vint = vector<int>;
using vll = vector<ll>;
using vld = vector<ld>;
using vpii = vector<pii>;
using vpil = vector<pil>;
using vpli = vector<pli>;
using vpll = vector<pll>;
using vb = vector<base>;

#define x first
#define y second
#define all(v) (v).begin(), (v).end()
#define sz(v) ((int)(v).size())
#define cpr(v) sort(all(v)); (v).erase(unique(all(v)), (v).end())
#define idx(v, x) int(lower_bound(all(v), (x)) - (v).begin())
#define ints(args...) int args; readln(args);
#define lls(args...) ll args; readln(args);
#define strs(args...) string args; readln(args);

template<typename... Args>
void readln(Args&... args) { ((cin >> args), ...); }
template<typename... Args>
void writeln(Args... args) { ((cout << args << " "), ...); cout << '\n'; }

map<vint, double> dp;
int n;

double solve(vint a){
  auto it = dp.find(a);
  if(it != dp.end()) return it->second;
  dp.insert({a, 0});
  it = dp.find(a);
  double& ret = it->second;
  int cnt=0;
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      if(a[i] <= a[j]) continue;
      cnt++;
      swap(a[i], a[j]);
      ret += solve(a) + 1;
      swap(a[i], a[j]);
    }
  }
  return ret /= cnt;
}
int main(void){
  cin>>n;
  vint a(n);
  for(int& i:a) cin>>i;
  vint b(a);
  sort(all(b));
  dp.insert({b, 0});
  printf("%.7lf", solve(a));
}