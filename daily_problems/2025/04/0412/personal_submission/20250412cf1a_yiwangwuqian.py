'''def main():
    n = II()
    nums = LII()

    dp = [0] * (n + 1)
    for v in nums:
        dp[v] = dp[v - 1] + 1

    print(n - max(dp))'''
def main():
    n = int(input())
    nums = list(map(int,input().split()))
    dp = [0]*(n+1)
    for v in nums:
        dp[v] = dp[v-1] + 1
    print(n - max(dp))
main()
