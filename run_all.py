"""
Run all steps of the Day22 Lab sequentially.
Usage:
  python run_all.py              # Run all steps
  python run_all.py --step 1     # Run specific step only
"""

import sys
import argparse
from pathlib import Path


def run_step_1():
    """Run Step 1: LangSmith RAG Pipeline"""
    print("\n" + "=" * 70)
    print("Running Step 1: LangSmith RAG Pipeline")
    print("=" * 70)
    import langsmith_rag_pipeline
    langsmith_rag_pipeline.main()


def run_step_2():
    """Run Step 2: Prompt Hub & A/B Routing"""
    print("\n" + "=" * 70)
    print("Running Step 2: Prompt Hub & A/B Routing")
    print("=" * 70)
    import prompt_hub_ab_routing
    prompt_hub_ab_routing.main()


def run_step_3():
    """Run Step 3: RAGAS Evaluation"""
    print("\n" + "=" * 70)
    print("Running Step 3: RAGAS Evaluation")
    print("=" * 70)
    print("⚠️  This step takes ~20-30 minutes. Please be patient.")
    import ragas_evaluation
    ragas_evaluation.main()


def run_step_4():
    """Run Step 4: Guardrails Validators"""
    print("\n" + "=" * 70)
    print("Running Step 4: Guardrails Validators")
    print("=" * 70)
    import guardrails_validator
    guardrails_validator.main()


def main():
    parser = argparse.ArgumentParser(description="Run Day22 Lab steps")
    parser.add_argument(
        "--step", 
        type=int, 
        choices=[1, 2, 3, 4],
        help="Run a specific step (1-4). If not provided, runs all steps."
    )
    args = parser.parse_args()

    steps = {
        1: run_step_1,
        2: run_step_2,
        3: run_step_3,
        4: run_step_4,
    }

    if args.step:
        # Run specific step
        steps[args.step]()
    else:
        # Run all steps
        print("=" * 70)
        print("Day22 Lab — LangSmith + Prompt Versioning")
        print("Running all steps sequentially...")
        print("=" * 70)
        
        for step_num in [1, 2, 3, 4]:
            try:
                steps[step_num]()
            except Exception as e:
                print(f"\n❌ Error in Step {step_num}: {e}")
                print("Stopping execution.")
                sys.exit(1)
        
        print("\n" + "=" * 70)
        print("✅ All steps completed successfully!")
        print("=" * 70)
        print("\nNext steps:")
        print("1. Collect evidence screenshots:")
        print("   - evidence/01_langsmith_traces.png")
        print("   - evidence/02_prompt_hub.png")
        print("   - evidence/02_ab_routing_log.txt")
        print("   - evidence/03_ragas_scores.png")
        print("   - evidence/03_ragas_report.json")
        print("   - evidence/04_pii_demo_log.txt")
        print("   - evidence/04_json_demo_log.txt")
        print("\n2. Submit your GitHub repo URL and LangSmith project URL")


if __name__ == "__main__":
    main()
