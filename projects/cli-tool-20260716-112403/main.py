#!/usr/bin/env python3
"""CLI Tool"""
import argparse

def main():
    parser = argparse.ArgumentParser(description='CLI Tool')
    parser.add_argument('--name', default='World', help='Name to greet')
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == '__main__':
    main()
