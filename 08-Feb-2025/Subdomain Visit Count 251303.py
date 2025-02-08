# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_lists ={}

        for domain in cpdomains:
            visited, main_domain = domain.split(' ')
            sub_domains = main_domain.split('.')[::-1]

            prev_domain = ''

            for dm in sub_domains:
                domain_dict =dm+prev_domain
                domains_lists[domain_dict] = domains_lists.get(domain_dict, 0) + int(visited)
                prev_domain=f'.{domain_dict}'
        
        result = []

        for key,value in domains_lists.items():
            result.append(f"{value} {key}")
        
        return result

