

def lcs(s1,s2):
    
    r = len(s1)
    c = len(s2)
    dp = [ [0] * [c+1] for _  in range(r+1) ]
    
    for i in range(1, r+1):
        for j in range(1, c+1):
            if s1[i][j] == s2[i][j]:
                #diagnoal if same
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                #max of above and left
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    
    return dp[r][c]