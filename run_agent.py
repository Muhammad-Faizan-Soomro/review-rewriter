from fetch_reviews import fetch_old_reviews
from groq_rewriter import rewrite_review
from update_reviews import update_review

print("📥 Fetching old reviews...")
reviews = fetch_old_reviews()

for review in reviews:
    print(f"\n📝 Review ID {review['id']} ({review['review_date']}):")
    print("Original:", review['review_text'])

    try:
        # STEP 0: Skip blank or very short reviews
        if not review['review_text'] or len(review['review_text'].strip()) == 0:
            print("⚠️ Skipped: Review empty.")
            continue

        # STEP 1: Get LLM output
        new_text = rewrite_review(review['review_text'])
        print("✨ Rewritten:", new_text)

        # STEP 2: Update database
        update_review(review['id'], new_text)
        print(f"✅ Review ID {review['id']} updated successfully.")

    except Exception as e:
        print(f"❌ Error processing Review ID {review['id']}")
        print("Error details:", str(e))
