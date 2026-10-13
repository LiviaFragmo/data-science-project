"""Reproduce the portfolio's descriptive findings using Python's standard library."""
import argparse, csv, json, math, statistics, urllib.request
from pathlib import Path

SOURCE = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, help='Optional locally downloaded course CSV')
    args = parser.parse_args()
    if args.data:
        stream = args.data.open()
    else:
        import io
        stream = io.StringIO(urllib.request.urlopen(SOURCE).read().decode('utf-8-sig'))
    rows = list(csv.DictReader(stream))
    x = [float(r['sqft_above']) for r in rows]
    y = [float(r['price']) for r in rows]
    mx, my = statistics.mean(x), statistics.mean(y)
    corr = sum((a-mx)*(b-my) for a,b in zip(x,y)) / math.sqrt(sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))
    groups = {str(k): [float(r['price']) for r in rows if int(r['waterfront']) == k] for k in (0,1)}
    result = {'rows': len(rows), 'area_price_correlation': corr, 'median_price_by_waterfront': {k: statistics.median(v) for k,v in groups.items()}, 'group_counts': {k: len(v) for k,v in groups.items()}}
    Path('results.json').write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
