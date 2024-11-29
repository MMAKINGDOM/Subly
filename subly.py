import dns.resolver
import asyncio
from rich.console import Console
from rich.color import Color
# Lets Start
# Initialize the rich console
console = Console()

# Print the header with rich
console.print(f'[green] __       _     _ [/green]')
console.print(f'[green]/ _\\_   _| |__ | |_   _ [/green]')
console.print(f'[green]\\ \\| | | | \'_ \\| | | | |[/green]')
console.print(f'[green]_-\\ \\ |_| | |_) | | |_| | [/green]')
console.print(f'[green]\\__/\\__,_|_.__/|_|\\__, |[/green]')
console.print(f'[green]                  |___/ [/green]')
console.print(f'[red]Made by Muntadhar M. Ahmed - @muntadharma [IG][/red]')

# Function to resolve subdomains
async def r_s(subd):
    try:
        dns.resolver.resolve(subd, 'A')
        console.print(f'[green][Found] {subd}[/green]')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass
    except Exception as e:
        abc = True

# Function to process file with subdomains
async def c_s_f_f(domain, file_path):
    with open(file_path, 'r') as file:
        subdomains = file.readlines()
    
    tasks = []
    for subd in subdomains:
        subd = subd.strip()
        full_subd = subd + '.' + domain
        task = asyncio.create_task(r_s(full_subd))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

# Main execution
if __name__ == '__main__':
    domain = input('Enter the Domain (e.g., google.com): ')
    file_path = 'names.txt'
    asyncio.run(c_s_f_f(domain, file_path))
