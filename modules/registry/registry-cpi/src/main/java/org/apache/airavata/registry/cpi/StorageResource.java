/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 * <p>
 * http://www.apache.org/licenses/LICENSE-2.0
 * <p>
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package org.apache.airavata.registry.cpi;

import org.apache.airavata.model.appcatalog.storageresource.StorageResourceDescription;

import java.util.List;
import java.util.Map;

public interface StorageResource {
    /**
     * This function will add a storage resource description to the database
     * @param description storage resource description
     * @return unique resource ID generated by airavata
     */
    String addStorageResource(StorageResourceDescription description) throws AppCatalogException;

    /**
     * This method will update storage resource
     * @param storageResourceId unique storage resource id
     * @param updatedStorageResource updated storage resource
     */
    void updateStorageResource(String storageResourceId, StorageResourceDescription updatedStorageResource) throws AppCatalogException;

    /**
     * This method will retrieve storage resource object on given resource id
     * @param resourceId unique resource id
     * @return StorageResource object
     */
    StorageResourceDescription getStorageResource(String resourceId) throws AppCatalogException;

    /**
     * This method will return a list of storageResource descriptions according to given search criteria
     * @param filters map should be provided as the field name and it's value
     * @return list of storage resources
     */
    List<StorageResourceDescription> getStorageResourceList(Map<String, String> filters) throws AppCatalogException;

    /**
     * This method will retrieve all the storage resources
     * @return list of storage resources
     * @throws AppCatalogException
     */
    List<StorageResourceDescription> getAllStorageResourceList() throws AppCatalogException;

    /**
     * This method will retrieve all the storage resource id with it's name
     * @return map of storage resource ids + name
     * @throws AppCatalogException
     */
    Map<String, String> getAllStorageResourceIdList() throws AppCatalogException;

    /**
     * This method will retrieve all the enabled storage resource id with it's name
     * @return
     * @throws AppCatalogException
     */
    Map<String, String> getAvailableStorageResourceIdList() throws AppCatalogException;

    /**
     * This method will check whether the given resource already exists in the system
     * @param resourceId unique resource id
     * @return true or false
     */
    boolean isStorageResourceExists(String resourceId) throws AppCatalogException;

    /**
     * This method will remove given resource from the system
     * @param resourceId unique resource id
     */
    void removeStorageResource(String resourceId) throws AppCatalogException;

    void removeDataMovementInterface(String storageResourceId, String dataMovementInterfaceId)  throws AppCatalogException;

}
