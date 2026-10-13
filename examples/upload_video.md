# Upload Video — Example

## Copy-paste

```bash
# Upload with dry-run (no real upload)
python3 ~/yt.py upload video.mp4 --title "My Video" --dry-run
```

## Expected Output

```
Video: video.mp4
Title: My Video
Mode: DRY-RUN
Would upload as: https://youtube.com/watch?v=mock123
```

## Safety

- Dry-run default
- Requires: `~/.youtube_token.json`
- Content ID only via Studio UI
