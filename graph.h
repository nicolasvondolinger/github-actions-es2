#ifndef GRAPH_H
#define GRAPH_H

#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

#define _ ios_base::sync_with_stdio(0); cin.tie(0);
#define all(a) (a).begin(), (a).end()
#define endl '\n'
#define ff first
#define ss second
#define pb push_back

typedef long long ll;
const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;

void dfs(int v, std::vector<bool>& visited, const std::vector<std::vector<int>>& graph);

int countComponents(int n, const std::vector<std::vector<int>>& graph);

#endif