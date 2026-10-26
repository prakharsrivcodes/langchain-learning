branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model |parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
)

