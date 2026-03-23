"""
Daily Papers fetcher - Auto fetch new papers and update repository
"""

import os
import sys
import glob
import shutil
import subprocess
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(__file__))

from paper_analysis import analyze_paper, generate_analysis_markdown

PAPERS_DIR = '/root/.openclaw/workspace/papers'
REPO_DIR = '/root/.openclaw/workspace/daily-papers'

def fetch_latest_papers():
    """Fetch latest papers using the existing fetch script"""
    from skills.paper_pusher.scripts.fetch_papers import fetch_papers
    
    date_str = datetime.now().strftime('%Y%m%d')
    output_path = os.path.join(PAPERS_DIR, f'papers_{date_str}.md')
    
    # Run the fetch script
    os.system(f'python3 /root/.openclaw/workspace/skills/paper-pusher/scripts/fetch_papers.py --days 1 --output {output_path}')
    
    return output_path


def copy_papers_to_app():
    """Copy latest papers to the app directory"""
    papers_files = glob.glob(os.path.join(PAPERS_DIR, 'papers_*.md'))
    
    if not papers_files:
        print("No papers found!")
        return False
    
    # Get latest file
    latest_file = max(papers_files, key=os.path.getmtime)
    target_file = os.path.join(REPO_DIR, 'papers', 'papers_latest.md')
    
    # Copy
    shutil.copy(latest_file, target_file)
    print(f"Copied {latest_file} to {target_file}")
    return True


def update_analysis():
    """Generate updated analysis"""
    from app import get_latest_papers, get_stats
    
    papers = get_latest_papers()
    stats = get_stats(papers)
    
    # Generate detailed analysis markdown
    analysis_md = generate_analysis_markdown(papers)
    
    analysis_file = os.path.join(REPO_DIR, 'papers', 'analysis_latest.md')
    with open(analysis_file, 'w', encoding='utf-8') as f:
        f.write(analysis_md)
    
    print(f"Generated analysis: {len(papers)} papers analyzed")
    return papers, stats


def commit_and_push():
    """Commit changes and push to GitHub"""
    # Token should be set via environment variable GITHUB_TOKEN
    token = os.environ.get('GITHUB_TOKEN', '')
    if not token:
        print("Warning: GITHUB_TOKEN not set, skipping push")
        return
    repo_url = f'https://woodszp:{token}@github.com/ZhipingWoods/daily-papers.git'
    
    commands = [
        'cd /root/.openclaw/workspace/daily-papers',
        'git add papers/ app.py',
        f'git commit -m "Update papers and analysis - {datetime.now().strftime("%Y-%m-%d %H:%M")}"',
        f'git push {repo_url} master'
    ]
    
    for cmd in commands:
        os.system(cmd)


def main():
    """Main workflow"""
    print("=" * 50)
    print("Daily Papers Update Workflow")
    print("=" * 50)
    
    # Step 1: Fetch latest papers
    print("\n[1/4] Fetching latest papers...")
    fetch_latest_papers()
    
    # Step 2: Copy to app
    print("\n[2/4] Copying papers to app...")
    copy_papers_to_app()
    
    # Step 3: Generate analysis
    print("\n[3/4] Generating paper analysis...")
    papers, stats = update_analysis()
    
    print(f"\n📊 Stats: {stats['total']} papers")
    for cat, count in stats['categories'].items():
        print(f"   {cat}: {count}")
    
    # Step 4: Push to GitHub
    print("\n[4/4] Pushing to GitHub...")
    # commit_and_push()  # Uncomment to auto-push
    
    print("\n✅ Update complete!")
    print(f"📁 Papers: {REPO_DIR}/papers/")


if __name__ == '__main__':
    main()