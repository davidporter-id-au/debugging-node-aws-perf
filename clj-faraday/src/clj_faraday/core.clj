(ns clj-faraday.core
  (:gen-class)
  (:require [taoensso.faraday :as far]))

(def cred
  {:endpoint "http://dynamodb.ap-southeast-2.amazonaws.com"
   :access-key (System/getenv "AWS_ACCESS_KEY")
   :secret-key (System/getenv "AWS_SECRET_KEY")})

(defn get-record [table key]
  (do
    (far/get-item cred :test {:key key}))
    "")

(defn -main
  [& args]
  (while true
    (println (time (get-record "test" "FOO")))
    (Thread/sleep 1000)))
