# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Rebuild ref_acronym_norm with grouped definitions
# MAGIC %sql
# MAGIC -- Re-builds ref_acronym_norm so every key gets ALL its distinct definitions
# MAGIC -- grouped into one enrichment_text string, e.g.:
# MAGIC --   Acronym: AC, Definitions: {Advanced countries, Assay Control}
# MAGIC --
# MAGIC -- Reads the current ref_acronym_norm (for key_norm / canonical_id)
# MAGIC -- and joins back to the raw source (Acronyms_other_deviations) to collect
# MAGIC -- every Medical/Industry definition for that acronym.
# MAGIC
# MAGIC CREATE OR REPLACE TABLE `us_gmsgq_dev`.`gms_us_alyt`.`ref_acronym_norm` AS
# MAGIC WITH all_defs AS (
# MAGIC     SELECT
# MAGIC         r.key_norm,
# MAGIC         r.entity_type,
# MAGIC         r.canonical_id,
# MAGIC         collect_set(
# MAGIC             REGEXP_REPLACE(REGEXP_REPLACE(REGEXP_REPLACE(REGEXP_REPLACE(
# MAGIC                 LOWER(TRIM(a.Definition)),
# MAGIC                 'isation', 'ization'),   -- centralisation -> centralization
# MAGIC                 'ised\\b',  'ized'),     -- decentralised  -> decentralized
# MAGIC                 'ising\\b', 'izing'),   -- authorising    -> authorizing
# MAGIC                 'ise\\b',   'ize')      -- normalise      -> normalize
# MAGIC         ) AS definitions
# MAGIC     FROM `us_gmsgq_dev`.`gms_us_alyt`.`ref_acronym_norm` r
# MAGIC     LEFT JOIN `us_gmsgq_dev`.`gms_us_alyt`.`Acronyms_other_deviations` a
# MAGIC         ON UPPER(TRIM(r.canonical_id)) = UPPER(TRIM(a.Acronym))
# MAGIC         AND a.Category IN ('Medical', 'Industry')
# MAGIC         AND a.Definition IS NOT NULL
# MAGIC         AND TRIM(a.Definition) != ''
# MAGIC     GROUP BY r.key_norm, r.entity_type, r.canonical_id
# MAGIC )
# MAGIC SELECT
# MAGIC     key_norm,
# MAGIC     entity_type,
# MAGIC     canonical_id,
# MAGIC     CONCAT(
# MAGIC         '[ACRONYM] "', key_norm, '"', '\n',
# MAGIC         'Canonical: ',  canonical_id, '\n',
# MAGIC         'Definitions: {',
# MAGIC         array_join(array_sort(definitions), ', '),
# MAGIC         '}'
# MAGIC     ) AS enrichment_text
# MAGIC FROM all_defs;

# COMMAND ----------

# DBTITLE 1,Verify British English fix
# MAGIC %sql
# MAGIC SELECT key_norm, enrichment_text
# MAGIC FROM `us_gmsgq_dev`.`gms_us_alyt`.`ref_acronym_norm`
# MAGIC WHERE enrichment_text LIKE '%decentraliz%'
# MAGIC    OR enrichment_text LIKE '%centraliz%'
# MAGIC    OR enrichment_text LIKE '%authoriz%'
# MAGIC    OR enrichment_text LIKE '%normaliz%'; 
