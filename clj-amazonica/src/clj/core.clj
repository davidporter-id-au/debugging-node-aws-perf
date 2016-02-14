(ns clj.core
  (:gen-class)
  (:require [amazonica.aws.dynamodbv2 :as dynamo]))

(defn get-record [table key]
  (do
    (dynamo/get-item {:endpoint "ap-southeast-2"} {:table-name table :key {:key {:s key}}} ))
    "")

(defn -main
  [& args]
  (while true
    (println (time (get-record "test" "FOO")))
    (Thread/sleep 1000)))
