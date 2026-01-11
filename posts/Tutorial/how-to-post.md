# How to Add a New Post

Adding a new post is simple:

## Step 1: Create the Markdown File

Create a new `.md` file in the `posts/` directory:

```
posts/my-new-post.md
```

Write your content using standard Markdown syntax.

## Step 2: Update posts.json

Add an entry to `posts.json`:

```json
{
    "title": "My New Post",
    "date": "2026-01-15",
    "file": "my-new-post.md",
    "categories": ["Category1", "Category2"],
    "summary": "A brief description of the post."
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| title | Yes | The post title |
| date | Yes | Publication date (YYYY-MM-DD) |
| file | Yes | Filename in posts/ directory |
| categories | No | Array of category names |
| summary | No | Short description for the list |

## Step 3: Add Images (Optional)

Put images in the `images/` folder and reference them:

```markdown
![My Image](images/photo.jpg)
```

## Step 4: Commit and Push

```bash
git add .
git commit -m "Add new post"
git push
```

Your post will be live on GitHub Pages!
