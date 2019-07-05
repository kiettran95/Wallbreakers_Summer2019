class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_domains = dict()
        for cpdomain in cpdomains:
            count,domains = cpdomain.split()
            domains = domains.split('.')
            i=len(domains)-1
            domain=domains[i]
            while True:
                if not domain in count_domains:
                    count_domains[domain]=0
                    
                count_domains[domain]+=int(count)
                i-=1
                if i==-1:
                    break
                domain=domains[i]+"."+domain
                
        ans=list()
        for domain,count in count_domains.items():
            ans.append(str(count) + " " + domain)
        return ans
