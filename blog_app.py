# -*- coding: utf-8 -*-
"""Project3 .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gY3O7cjph7YVkVTf5fFpuE4t8mUypcGr
"""

import os
from datetime import datetime

# Directory to store blog posts
BLOG_DIR = "blog_posts"
os.makedirs(BLOG_DIR, exist_ok=True)

# Function to generate a unique ID
def generate_id():
    files = os.listdir(BLOG_DIR)
    return len(files) + 1

# Function to save a blog post
def save_post(post):
    filename = f"{BLOG_DIR}/{post['id']}.txt"
    with open(filename, "w") as f:
        f.write(format_post(post))
    print(f"Blog post saved as {filename}")

# Function to format a blog post
def format_post(post):
    post_template = (f"ID: {post['id']}\n"
                     f"Title: {post['title']}\n"
                     f"Category: {post['category']}\n"
                     f"Tags: {', '.join(post['tags'])}\n"
                     f"Published: {post['published']}\n"
                     f"Last Updated: {post.get('updated', 'N/A')}\n"
                     f"Content:\n{post['content']}\n")
    return post_template

# Function to create a new blog post
def create_post():
    post = {
        "id": generate_id(),
        "title": input("Enter title: "),
        "category": input("Enter category: "),
        "tags": input("Enter tags (comma-separated): ").split(","),
        "published": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated": "N/A",
        "content": input("Enter content: ")
    }
    save_post(post)

# Function to update an existing blog post
def update_post(post_id):
    filename = f"{BLOG_DIR}/{post_id}.txt"
    if not os.path.exists(filename):
        print("Post not found!")
        return


    with open(filename, "r") as f:
        lines = f.readlines()
        content_index = lines.index("Content:\n") + 1
        content = "".join(lines[content_index:])

    post = {
        "id": post_id,
        "title": input("Enter new title: ") or lines[1].split(": ")[1].strip(),
        "category": input("Enter new category: ") or lines[2].split(": ")[1].strip(),
        "tags": input("Enter new tags (comma-separated): ") or lines[3].split(": ")[1].strip(),
        "published": lines[4].split(": ")[1].strip(),
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "content": input("Enter new content: ") or content
    }
    save_post(post)

# Function to delete a blog post
def delete_post(post_id):
    filename = f"{BLOG_DIR}/{post_id}.txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("Blog post deleted successfully.")
    else:
        print("Post not found!")

# Function to search blog posts
def search_posts(term):
    for file in os.listdir(BLOG_DIR):
        if file.endswith(".txt"):
            with open(f"{BLOG_DIR}/{file}", "r") as f:
                content = f.read()
                if term.lower() in content.lower():
                    print("=" * 50)
                    print(content)
                    print("=" * 50)

# Function to display all blog posts
def view_posts():
    for file in os.listdir(BLOG_DIR):
        if file.endswith(".txt"):
            with open(f"{BLOG_DIR}/{file}", "r") as f:
                print("=" * 50)
                print(f.read())
                print("=" * 50)

# Main program loop
def main():
    while True:
        print("\n1. Create Post\n2. Update Post\n3. Delete Post\n4. View Posts\n5. Search Posts\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            create_post()
        elif choice == "2":
            update_post(input("Enter post ID to update: "))
        elif choice == "3":
            delete_post(input("Enter post ID to delete: "))
        elif choice == "4":
            view_posts()
        elif choice == "5":
            search_posts(input("Enter search term: "))
        elif choice == "6":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

